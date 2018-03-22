from __future__ import absolute_import

from linode.objects import DerivedBase, Property


class DomainRecord(DerivedBase):
    api_endpoint = "/domains/{domain_id}/records/{id}"
    derived_url_path = "records"
    parent_id_name = "domain_id"

    properties = {
        'id': Property(identifier=True),
        'domain_id': Property(identifier=True),
        'type': Property(),
        'name': Property(mutable=True, filterable=True),
        'target': Property(mutable=True, filterable=True),
        'priority': Property(mutable=True),
        'weight': Property(mutable=True),
        'port': Property(mutable=True),
        'service': Property(mutable=True),
        'protocol': Property(mutable=True),
        'ttl_sec': Property(mutable=True),
    }
