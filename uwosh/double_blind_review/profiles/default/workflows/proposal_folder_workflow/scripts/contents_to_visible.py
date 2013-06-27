## Script (Python) "contents_to_visible"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=thisfolder
##title=contents_to_visible
##
#This script calles trusted code to transition the contents of a proposal drop
#box to visible versions of their various states.
# J. Gutow June 26 2013

from uwosh.double_blind_review.make_decisions_visible import make_decisions_visible
make_decisions_visible(thisfolder.object)

