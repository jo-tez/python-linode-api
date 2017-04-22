from .. import DerivedBase, Property

class TicketReply(DerivedBase):
    api_name = 'replies'
    api_endpoint = '/support/tickets/{ticket_id}/replies'
    derived_url_path = 'replies'
    parent_id_name='ticket_id'

    properties = {
        'id': Property(identifier=True),
        'ticket_id': Property(identifier=True),
        'description': Property(),
        'created': Property(),
        'created_by': Property(),
    }