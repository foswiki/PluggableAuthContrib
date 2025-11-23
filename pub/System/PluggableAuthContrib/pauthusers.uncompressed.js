/*
Foswiki - The Free and Open Source Wiki, http://foswiki.org/

Copyright (C) 2022-2025 Michael Daum

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version. For
more details read LICENSE in the root of this distribution.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

As per the GPL, removal of this notice is prohibited.

*/

"use strict";
(function($) {

  var defaults = {},
      pauthUsers;

  function PauthUsers(elem, opts) {
    var self = this;

    self.elem = $(elem);
    self.opts = $.extend(true, defaults, self.elem.data(), opts);
    self.init();
  }

  PauthUsers.prototype.init = function () {
    var self = this;

    //console.log("loading pauthUsers inerface");

    self.sidebar = $(".pauthSideBar");
    self.addUserButton = self.elem.find(".pauthAddUser"),
    self.addGroupButton = self.elem.find(".pauthAddGroup"),
    self.updateButton = self.elem.find(".pauthUpdateUser"),
    self.groupsButton = self.elem.find(".pauthGroups"),
    self.passwordButton = self.elem.find(".pauthChangePassword"),
    self.resetButton = self.elem.find(".pauthResetPassword"),
    self.deleteButton = self.elem.find(".pauthDeleteUser"),
    self.activateButton = self.elem.find(".pauthActivateUser"),
    self.deactivateButton = self.elem.find(".pauthDeactivateUser"),
    self.table = self.elem.find(".pauthUsersTable table");
    self.dataTable = self.table.data("dt"),
    self.selectionElem = self.elem.find("input[name=id]");

    self.dataTable.on("dblclick", "tr", function() {
      var data = self.dataTable.row(this).data();

      if (!data) {
        return;
      }

      foswiki.loadTemplate({
        "name": "System.PluggableAuthUsers",
        "expand": "pauth::edituserdialog",
        "uid": data.id.raw
      }).done(function(data) {
        var $content = $(data.expand);
        $("body").append($content);
      });

      return false;
    });

    self.dataTable.on("select deselect", function() {
       var selection = self.getSelection();

       //console.log("selection=",selection);
       if (selection.length === 0) {
          self.updateButton.addClass("jqButtonDisabled");
          self.passwordButton.addClass("jqButtonDisabled");
          self.deleteButton.addClass("jqButtonDisabled");
          self.activateButton.addClass("jqButtonDisabled");
          self.deactivateButton.addClass("jqButtonDisabled");
          self.resetButton.addClass("jqButtonDisabled");
          self.groupsButton.addClass("jqButtonDisabled");
       } else if (selection.length === 1) {
          self.updateButton.removeClass("jqButtonDisabled");
          self.passwordButton.removeClass("jqButtonDisabled");
          self.deleteButton.removeClass("jqButtonDisabled");
          self.activateButton.removeClass("jqButtonDisabled");
          self.deactivateButton.removeClass("jqButtonDisabled");
          self.resetButton.removeClass("jqButtonDisabled");
          self.groupsButton.removeClass("jqButtonDisabled");
       } else {
          self.updateButton.addClass("jqButtonDisabled");
          self.groupsButton.addClass("jqButtonDisabled");
          self.passwordButton.addClass("jqButtonDisabled");
          self.deleteButton.removeClass("jqButtonDisabled");
          self.activateButton.removeClass("jqButtonDisabled");
          self.deactivateButton.removeClass("jqButtonDisabled");
          self.resetButton.removeClass("jqButtonDisabled");
       }
    });

    self.dataTable.on("preXhr.dt", function(ev, settings, data) {
      var gid = self.getSelectedGroup();

      if (gid) {
        data.query += " and m.gid='"+gid+"'";
      }

      //console.log("query=",data.query);
    });

    $(".pauthSideBar .selected .pauthGroupLink").each(function() {
        var text  = $(this).text().trim();
        $(".pauthGroupFilter").html("( "+ text + " )");
    });
  };

  PauthUsers.prototype.getSelection = function() {
    var self = this,
        val = self.selectionElem.val(),
        selection = (val === "") ? [] : val.split(/\s*,\s*/);

    return selection;
  };

  PauthUsers.prototype.clearSelection = function() {
    var self = this;

    //console.log("clearing selection",self.selectionElem[0]);
    self.dataTable.rows().deselect();
    self.selectionElem.val("");
  };

  PauthUsers.prototype.getSelectedGroup = function() {
    var self = this;

    return self.sidebar.find(".selected .pauthGroupLink").data("gid");
  };

  PauthUsers.prototype.reloadSideBar = function() {
    var self = this;

    self.sidebar.trigger("refresh", {
      "selected": self.getSelectedGroup()
    });
  };

  PauthUsers.prototype.reloadTable = function() {
    var self = this;

    self.clearSelection();
    self.dataTable.ajax.reload();
  };

  // dialogs
  $(".pauthDialog").livequery(function() {
    var $form = $(this).find("form:first"),
        doReloadSideBar = $form.data("reloadSidebar"),
        $dialog = $(this);

    //console.log("new dialog");

    $form.on("beforeSubmit", function() {
      $dialog.dialog("destroy");
    });

    $form.on("success", function(ev, diag, response) {
      //console.log("reloading table ...");

      $.pnotify({
        type: "success",
        title: "Success",
        delay: 5000,
        text: response.result
      });

      pauthUsers.reloadTable();
      if (doReloadSideBar) {
        pauthUsers.reloadSideBar();
      }
    });

    $form.on("complete", function() {
      //console.log("removing old dialog ...");
      $dialog.remove();
    });
  });

  // pauthGroupLink
  $(document).on("click", ".pauthGroupLink", function() {
    var $this = $(this), 
        $li = $this.parent();

    $(".pauthSideBar .selected").removeClass("selected");
    $li.addClass("selected");
    $(".pauthGroupFilter").html("( "+$this.text().trim()+" )");

    pauthUsers.reloadTable();
    return false;
  });

  // pauthButton
  $(document).on("click", ".pauthButton", function() {
    var $button = $(this),
        opts = $.extend({
          "name": "System.PluggableAuthUsers",
          "uid": pauthUsers.getSelection().join(", ")
        }, $button.data());

    opts.expand = opts.dialog;
    delete opts.dialog;

    if ($button.is(".jqButtonDisabled")) {
      return false;
    }

    //console.log("clicked button");
    $button.parent().block({message:null});

    foswiki.loadTemplate(opts).done(function(data) {
      var $content = $(data.expand);
      $("body").append($content);
      $button.parent().unblock();
    });

    return false;
  });

  // Enable declarative widget instanciation
  $(function() {
    $(".pauthUsers").livequery(function() {
      pauthUsers = new PauthUsers(this);
    });

    $(".pauthProviderFilter").livequery(function() {
        var $input = $(this),
            $twisty = $input.prev(),
            opts = $input.data(),
            $target = $(opts.target);

        $twisty.on("afterClose.twisty", function() {
          $input.data("val", $input.val());
          $input.val("").trigger("keyup");
        }).on("beforeOpen.twisty", function() {
          var val = $input.data("val");
          if (typeof(val) !== 'undefined') {
            $input.val(val).data("val", undefined);
            $input.trigger("keyup");
          }
        }).on("afterOpen.twisty", function() {
          $input.focus();
        });

        $input.on("keyup", function() {
            var val = $input.val(), regex;

            if (val === "") {
              $target.children().show();
              return;
            }

            regex = new RegExp(val, "i");

            $target.children().each(function() {
                var $item = $(this), 
                    text = $item.text();

                if (regex.test(text)) {
                  $item.show();
                } else {
                  $item.hide();
                }
            });
        });
    });
  });


})(jQuery);
