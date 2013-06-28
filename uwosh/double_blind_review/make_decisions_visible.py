# This trusted code is meant to be used with the double blind review workflows
# to automatically transition the contents of a container to their final
# visible states.
# J. Gutow June 26, 2013

# Subscribe to the workflow transition completed action
from five import grok
from Products.DCWorkflow.interfaces import IAfterTransitionEvent
from Products.CMFCore.interfaces import IFolderish

@grok.subscribe(IFolderish, IAfterTransitionEvent)
def make_decisions_visible(context,event):
    #context.plone_log("context: "+str(context))
    #context.plone_log("status:"+str(event.status))
    if (event.status['review_state'] != 'cycle_complete'):
        #context.plone_log("state:"+str(event.status['review_state'])+". Nothing to do")
        #nothing to do
        return
    children = context.getFolderContents()
    wftool = context.portal_workflow

#loop through the children objects
    for obj in children:
        #context.plone_log("Examining "+str(obj.id))
        #context.plone_log("The object is: "+str(obj))
        #context.plone_log("The result of context[obj.id] is "+str(what))
        #context.plone_log("Available workflows:"+str(wftool.listWorkflows()))
        #transition each object
        state = obj.review_state
        #context.plone_log("The state is "+str(state))
        #context.plone_log("The state using getInfoFor: "+str(wftool.getInfoFor(what, 'review_state')))
        if (state=="alternate_invisible"):
            #context.plone_log("Identified and trying to transition proposal in the state: alternate_invisible.")
            # below is workaround for using getFolderContents() which provides a
            # 'brain' rather than an python object.  Inside if to avoid overhead
            # of getting object if do not need it.
            what = context[obj.id]
            wftool.doActionFor(what, 'to_alternate')
            reviews_to_cycle_complete(what)
        elif (state=="denied_invisible"):
            #context.plone_log("Identified and trying to transition proposal in the state: denied_invisible.")
            what = context[obj.id]
            wftool.doActionFor(what, 'to_denied')
            reviews_to_cycle_complete(what)
        elif (state=="approved_invisible"):
            #context.plone_log("Identified and trying to transition proposal in the state: approved_invisible.")
            what = context[obj.id]
            wftool.doActionFor(what, 'to_approved')
            reviews_to_cycle_complete(what)

def reviews_to_cycle_complete(proposal):
    children = proposal.getFolderContents()
    wftool = proposal.portal_workflow
#loop through the children objects
    for obj in children:
        state = obj.review_state
        if (state == 'panel_review'):
            what = proposal[obj.id]
            wftool.doActionFor(what, 'to_cycle_complete')

