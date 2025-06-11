{% macro clean_column_name(name) %}
    {{ name | lower | replace(' ', '_') | replace('.', '_') }}
{% endmacro %}
