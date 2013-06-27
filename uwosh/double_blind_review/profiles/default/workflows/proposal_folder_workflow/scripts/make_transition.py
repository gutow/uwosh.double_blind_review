## Script (Python) "make_transition"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=object,transition
##title=make_transition
##
# this little script is to work around the fact that you cannot get object information
# and have the correct proxy role to make transitions. 
context.plone_log("Calling "+str(object.content_status_modify))
context.plone_log("Object is "+str(object.id))
context.plone_log("review state is "+ str(object.review_state))
context.plone_log("transition is "+str(transition))
#actions = object.portal_workflow.getActionsFor(object)
#context.plone_log("available actions "+str(actions))
#object.content_status_modify("workflow_action="+transition)
objWF = context.portal_workflow.getWorkflowsFor(object)
#objWF = context.portal_workflow.getInfoFor(object,'review_state')
context.plone_log("work flow is "+str(objWF))
objTR = context.portal_workflow.getTransitionsFor(object)
context.plone_log("transitions are: "+str(objTR))
context.plone_log("context is "+str(context))
WF = context.portal_workflow.listWorkflows()
context.plone_log("work flows are "+str(WF))
context.portal_workflow.doActionFor(object, transition, wf_id='proposal_workflow')
