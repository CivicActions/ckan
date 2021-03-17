from typing import Dict
from ckan.logic import Context, DataDict

def package_create(context: Context, data_dict: DataDict) -> Dict: ...
def resource_create(context: Context, data_dict: DataDict) -> Dict: ...
def resource_view_create(context: Context, data_dict: DataDict) -> Dict: ...
def resource_create_default_resource_views(
    context: Context, data_dict: DataDict
) -> Dict: ...
def package_create_default_resource_views(
    context: Context, data_dict: DataDict
) -> Dict: ...
def package_relationship_create(
    context: Context, data_dict: DataDict
) -> Dict: ...
def member_create(context: Context, data_dict: DataDict) -> Dict: ...
def package_collaborator_create(
    context: Context, data_dict: DataDict
) -> Dict: ...
def group_create(context: Context, data_dict: DataDict) -> Dict: ...
def organization_create(context: Context, data_dict: DataDict) -> Dict: ...
def rating_create(context: Context, data_dict: DataDict) -> Dict: ...
def user_create(context: Context, data_dict: DataDict) -> Dict: ...
def user_invite(context: Context, data_dict: DataDict) -> Dict: ...
def vocabulary_create(context: Context, data_dict: DataDict) -> Dict: ...
def activity_create(context: Context, data_dict: DataDict) -> Dict: ...
def tag_create(context: Context, data_dict: DataDict) -> Dict: ...
def follow_user(context: Context, data_dict: DataDict) -> Dict: ...
def follow_dataset(context: Context, data_dict: DataDict) -> Dict: ...
def group_member_create(context: Context, data_dict: DataDict) -> Dict: ...
def organization_member_create(
    context: Context, data_dict: DataDict
) -> Dict: ...
def follow_group(context: Context, data_dict: DataDict) -> Dict: ...
def api_token_create(context: Context, data_dict: DataDict) -> Dict: ...