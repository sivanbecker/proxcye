from cob.project import get_project
import gossip


@gossip.register('cob.after_configure_app')
def after_configure_app(app):

    get_project().config['requests'] = {}
