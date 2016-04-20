/*
 * This file is part of Invenio.
 * Copyright (C) 2015 CERN.
 *
 * Invenio is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
 */


define(
  [
    'jquery',
    'flight',
    'hgn!js/workflows/templates/alert'
  ],
  function(
    $,
    flight,
    tpl_alert_src) {

    "use strict";

    return flight.component(WorkflowsUICommon);

    /**
    * .. js:class:: WorkflowsUICommon()
    *
    * Common utilities throughout workflows ui.
    *
    * :param string alertSelector:
    *
    */
    function WorkflowsUICommon() {
      this.attributes({
        // URL
        alertSelector: "#alert-message"
      });


      this.after('initialize', function() {
        this.on(document, "updateAlertMessage", function (ev, data) {
        $(this.attr.alertSelector).html(tpl_alert_src({
          category: data.category,
          message: data.message
        }));});
        console.log("Common init");
      });
    }
  }
);
