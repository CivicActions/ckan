"""
This type stub file was generated by pyright.
"""

import logging
import sys
import cgitb
import warnings
import xml.dom.minidom
import requests
import ckan.model as model
import ckan.plugins as p
import ckan.logic as logic
from __future__ import print_function
from ckan.lib.search.common import (
    SearchError,
    SearchIndexError,
    SearchQueryError,
    SolrSettings,
    is_available,
    make_connection,
)
from ckan.lib.search.index import NoopSearchIndex, PackageSearchIndex
from ckan.lib.search.query import (
    PackageSearchQuery,
    QueryOptions,
    ResourceSearchQuery,
    TagSearchQuery,
    convert_legacy_parameters_to_solr,
)

log = logging.getLogger(__name__)

def text_traceback(): ...

SUPPORTED_SCHEMA_VERSIONS = ["2.8", "2.9"]
DEFAULT_OPTIONS = {
    "limit": 20,
    "offset": 0,
    "order_by": "rank",
    "return_objects": False,
    "ref_entity_with_attr": "name",
    "all_fields": False,
    "search_tags": True,
    "callback": None,
}
_INDICES = {"package": PackageSearchIndex}
_QUERIES = {
    "tag": TagSearchQuery,
    "resource": ResourceSearchQuery,
    "package": PackageSearchQuery,
}
SOLR_SCHEMA_FILE_OFFSET_MANAGED = "/schema?wt=schema.xml"
SOLR_SCHEMA_FILE_OFFSET_CLASSIC = "/admin/file/?file=schema.xml"

def index_for(_type):
    """Get a SearchIndex instance sub-class suitable for
    the specified type."""
    ...

def query_for(_type):
    """Get a SearchQuery instance sub-class suitable for the specified
    type."""
    ...

def dispatch_by_operation(entity_type, entity, operation):
    """Call the appropriate index method for a given notification."""
    ...

class SynchronousSearchPlugin(p.SingletonPlugin):
    """Update the search index automatically."""

    def notify(self, entity, operation): ...

def rebuild(
    package_id=...,
    only_missing=...,
    force=...,
    refresh=...,
    defer_commit=...,
    package_ids=...,
    quiet=...,
):
    """
    Rebuilds the search index.

    If a dataset id is provided, only this dataset will be reindexed.
    When reindexing all datasets, if only_missing is True, only the
    datasets not already indexed will be processed. If force equals
    True, if an exception is found, the exception will be logged, but
    the process will carry on.
    """
    ...

def commit(): ...
def check(): ...
def show(package_reference): ...
def clear(package_reference): ...
def clear_all(): ...
def check_solr_schema_version(schema_file=...):
    """
    Checks if the schema version of the SOLR server is compatible
    with this CKAN version.

    The schema will be retrieved from the SOLR server, using the
    offset defined in SOLR_SCHEMA_FILE_OFFSET_MANAGED
    ('/schema?wt=schema.xml'). If SOLR is set to use the manually
    edited `schema.xml`, the schema will be retrieved from the SOLR
    server using the offset defined in
    SOLR_SCHEMA_FILE_OFFSET_CLASSIC ('/admin/file/?file=schema.xml').

    The schema_file parameter allows to override this pointing to
    different schema file, but it should only be used for testing
    purposes.

    If the CKAN instance is configured to not use SOLR or the SOLR
    server is not available, the function will return False, as the
    version check does not apply. If the SOLR server is available,
    a SearchError exception will be thrown if the version could not
    be extracted or it is not included in the supported versions list.

    :schema_file: Absolute path to an alternative schema file. Should
                  be only used for testing purposes (Default is None)
    """
    ...