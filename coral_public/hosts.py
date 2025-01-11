import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"coral_public"), "coral_public.urls", name="coral_public"),
)
