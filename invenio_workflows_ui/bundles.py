# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Workflows bundles."""

from __future__ import absolute_import, print_function

from flask_assets import Bundle

from invenio_assets import NpmBundle, RequireJSFilter

from werkzeug.local import LocalProxy

# NOTE:
# Here we exclude base JS bundles like jQuery etc. so that there does
# not exist several jQuery instances on the site.
try:
    from invenio_theme.bundles import js as _js
    exclude_js = [_js.contents[1]]
except ImportError:
    from flask import current_app
    try:
        exclude_js = LocalProxy(
            lambda: current_app.config['THEME_BASE_BUNDLES_EXCLUDE_JS']
        )
    except KeyError:
        import warnings
        warnings.warn(message=(
            "You are missing THEME_BASE_BUNDLES_EXCLUDE_JS from "
            "your configuration, which may cause you to have multiple instances"
            "of libraries like jQuery on your site."
        ))
        exclude_js = []


js_list = NpmBundle(
    'js/workflows/init.js',
    filters=RequireJSFilter(exclude=exclude_js),
    output='gen/workflowsui.list.%(version)s.js',
    npm={
        "prismjs": "~1.4.1",
        "flightjs": "~1.5.0",
        "hogan.js": "~3.0.2",
        "requirejs-hogan-plugin": "~0.3.1",
        "selectize": "0.12.1"
    }
)

js_details = NpmBundle(
    'js/workflows/details/init.js',
    filters=RequireJSFilter(exclude=exclude_js),
    output='gen/workflowsui.details.%(version)s.js',
    npm={
        "prismjs": "~1.4.1",
        "flightjs": "~1.5.0",
        "hogan.js": "~3.0.2",
        "requirejs-hogan-plugin": "~0.3.1",
    }
)

css = Bundle(
    'node_modules/prismjs/themes/prism.css',
    'node_modules/selectize/dist/css/selectize.bootstrap3.css',
    'css/workflows/workflows.css',
    filters='scss, cleancss',
    output='gen/workflowsui.%(version)s.css',
)
