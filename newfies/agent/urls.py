#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import patterns


urlpatterns = patterns('agent.views',
    (r'^agent_dashboard/$', 'agent_dashboard'),
    (r'^agent_detail_change/$', 'agent_detail_change'),

    (r'^agent/$', 'agent_list'),
    (r'^agent/add/$', 'agent_add'),
    #(r'^agent/contact_count/$', 'get_agent_count'),
    #(r'^agent/del/(.+)/$', 'agent_del'),
    #(r'^agent/(.+)/$', 'agent_change'),
)