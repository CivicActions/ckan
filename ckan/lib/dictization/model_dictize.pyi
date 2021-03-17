"""
This type stub file was generated by pyright.
"""

"""
These dictize functions generally take a domain object (such as Package) and
convert it to a dictionary, including related objects (e.g. for Package it
includes PackageTags, PackageExtras, PackageGroup etc).

The basic recipe is to call:

    dictized = ckan.lib.dictization.table_dictize(domain_object)

which builds the dictionary by iterating over the table columns.
"""

def group_list_dictize(
    obj_list,
    context,
    sort_key=...,
    reverse=...,
    with_package_counts=...,
    include_groups=...,
    include_tags=...,
    include_extras=...,
): ...
def resource_list_dictize(res_list, context): ...
def extras_dict_dictize(extras_dict, context): ...
def extras_list_dictize(extras_list, context): ...
def resource_dictize(res, context): ...
def package_dictize(pkg, context):
    """
    Given a Package object, returns an equivalent dictionary.
    """
    ...

def get_group_dataset_counts():
    """For all public groups, return their dataset counts, as a SOLR facet"""
    ...

def group_dictize(
    group,
    context,
    include_groups=...,
    include_tags=...,
    include_users=...,
    include_extras=...,
    packages_field=...,
    **kw
):
    """
    Turns a Group object and related into a dictionary. The related objects
    like tags are included unless you specify it in the params.

    :param packages_field: determines the format of the `packages` field - can
    be `datasets`, `dataset_count` or None.
    """
    ...

def tag_list_dictize(tag_list, context): ...
def tag_dictize(tag, context, include_datasets=...): ...
def user_list_dictize(obj_list, context, sort_key=..., reverse=...): ...
def member_dictize(member, context): ...
def user_dictize(
    user, context, include_password_hash=..., include_plugin_extras=...
): ...
def task_status_dictize(task_status, context): ...
def group_to_api(group, context): ...
def tag_to_api(tag, context): ...
def resource_dict_to_api(res_dict, package_id, context): ...
def package_to_api(pkg, context): ...
def vocabulary_dictize(vocabulary, context, include_datasets=...): ...
def vocabulary_list_dictize(vocabulary_list, context): ...
def activity_dictize(activity, context, include_data=...): ...
def activity_list_dictize(activity_list, context, include_data=...): ...
def package_to_api1(pkg, context): ...
def package_to_api2(pkg, context): ...
def group_to_api1(group, context): ...
def group_to_api2(group, context): ...
def tag_to_api1(tag, context): ...
def tag_to_api2(tag, context): ...
def user_following_user_dictize(follower, context): ...
def user_following_dataset_dictize(follower, context): ...
def user_following_group_dictize(follower, context): ...
def resource_view_dictize(resource_view, context): ...
def resource_view_list_dictize(resource_views, context): ...
def api_token_dictize(api_token, context): ...
def api_token_list_dictize(tokens, context): ...