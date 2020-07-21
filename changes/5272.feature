Users can now upload or link to custom profile pictures. By default, if a user picture is not provided it will fall back to gravatar. Alternatively, gravatar can be completely disabled by setting ``ckan.gravatar_default = disabled``. In that case a placeholder image is shown instead, which can be customized by overriding the ``templates/user/snippets/placeholder.html`` template.