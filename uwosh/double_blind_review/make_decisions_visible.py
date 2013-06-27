## Script (Python) "make_decisions_visible"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=thisfolder
##title=make_decisions_visible
##
#Be able to check this is a folderish object
#from Products.CMFCore.interfaces import IFolderish
#from Products.CMFCore.WorkflowCore import WorkflowException
#retrieve children objects
#if IFolderish.providedBy(context):

# This trusted code can be called by a workflow script to make state specific
# transitions of the contents of a container.
# J. Gutow June 26 2013

def make_decisions_visible(folder):
#folder = thisfolder.object
#context.plone_log("folder:"+str(folder))
    children = folder.getFolderContents()
    wftool = folder.portal_workflow
#context.plone_log("wftool= "+str(wftool))

#loop through the children objects
    for obj in children:
#   context.plone_log("Examining "+str(obj.id))
   #transition each object
        state = obj.review_state
#   context.plone_log("The state is "+str(state))
#   actions = wftool.getActionsFor(obj)
#   actions = obj.actions
#   context.plone_log("actions are:"+str(actions))
        if (state=="alternate_invisible"):
#      state = wftool.doActionFor(obj, 'to_alternate')
#          context.plone_log("Identified and trying to transition proposal in the state: alternate_invisible.")
            wftool.doActionFor(obj, 'to_alternate')
#      container.make_transition(obj, "to_alternate")
#      obj.content_status_modify(workflow_action='to_alternate')
#       state = obj.trans_ition(obj, transition="to_alternate")
        elif (state=="denied_invisible"):
            wftool.doActionFor(obj, 'to_denied')
        elif (state=="approved_invisible"):
            wftool.doActionFor(obj, 'to_approved')

