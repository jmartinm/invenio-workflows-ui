# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
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

"""Config variables for workflows UI module."""

from __future__ import absolute_import, print_function

WORKFLOWS_UI_URL = "/workflows"
WORKFLOWS_UI_API_URL = "/api/workflows/"

WORKFLOWS_UI_REST_ENDPOINT = dict(
    workflow_object_serializers={
        'application/json': ('invenio_workflows_ui.serializers'
                             ':json_serializer'),
    },
    search_serializers={
        'application/json': ('invenio_workflows_ui.serializers'
                             ':json_search_serializer'),
    },
    action_serializers={
        'application/json': ('invenio_workflows_ui.serializers'
                             ':json_action_serializer'),
    },
    bulk_action_serializers={
        'application/json': ('invenio_workflows_ui.serializers'
                             ':json_action_serializer'),
    },
    list_route='/workflows/',
    item_route='/workflows/<object_id>',
    search_index="workflows",
    default_media_type='application/json',
    max_result_window=10000,
)

WORKFLOWS_UI_DATA_TYPES = dict(
    workflow=dict(
        search_index='workflows',
        search_type='record',
    ),
)

WORKFLOWS_UI_CACHE_PREFIX = "WorkflowsUI::"
WORKFLOWS_UI_LIST_TEMPLATE = "invenio_workflows_ui/list.html"
WORKFLOWS_UI_DETAILS_TEMPLATE = "invenio_workflows_ui/details.html"
WORKFLOWS_UI_LIST_ROW_TEMPLATE = "invenio_workflows_ui/list_row.html"
WORKFLOWS_UI_INDEX_TEMPLATE = "invenio_workflows_ui/index.html"
