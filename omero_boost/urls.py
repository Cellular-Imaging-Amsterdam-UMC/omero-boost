#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from . import views

urlpatterns = [
    # API URLs
    path("api/list_dir/",
         views.list_directory,
         name="list_directory"),
    path("api/file_info/",
         views.file_info,
         name="file_info"),
    path("api/import_selected/",
         views.import_selected,
         name="import_selected"),
    path("api/biomero/admin/config/",
         views.get_biomero_config,
         name="get_biomero_config"),
    path("api/biomero/workflows/",
         views.list_workflows,
         name="list_workflows"),
    path("api/biomero/workflows/<str:name>/metadata/",
         views.get_workflow_metadata,
         name="get_workflow_metadata"),
    path("api/biomero/workflows/<str:name>/github/",
         views.get_workflow_github,
         name="get_workflow_github"),
    path("api/biomero/workflows/run/",
         views.run_workflow_script,
         name="run_workflow_script"),  # POST
    path("api/biomero/admin/config/save/",
         views.save_biomero_config,
         name="save_biomero_config"),  # POST
    # Webclient URLs
#     path("upload/",
#          views.omero_boost_upload,
#          name="omero_boost_upload"),
    path("local_file_browser/",
         views.get_folder_contents,
         name="local_file_browser",
         ),
    path("canvas/",
         views.canvas,
         name="canvas",
         ),
    # Webclient templates and script menu
    re_path(r"^webclient_templates/(?P<base_template>[a-z0-9_]+)/",
            views.webclient_templates,
            name="webclient_templates",
            ),
    re_path(r"^get_script_menu/$",
            views.get_script_menu,
            name="get_script_menu"),
]
