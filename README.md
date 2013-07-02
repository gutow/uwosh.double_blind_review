uwosh.double_blind_review
=========================

uwosh.double_blind_review

Introduction
============
This product product provides workflows and some test types for providing 
double-blind reviews of plone content items.

In addition to special workflows the following root templates are modified to 
prevent all but managers and owners from see identifying information.
   contenthistory - located in this product at 
      uwosh.double_blind_review/uwosh/double_blind_review/static/overrides/plone.app.layout.viewlets.content_history.pt
   plone.belowcontenttitle.documentbyline - located in this product at 
      uwosh.double_blind_review/uwosh/double_blind_review/static/overrides/plone.app.layout.viewlets.document_byline.pt
      
Overview of what this product does
==================================
*Target Uses 
This product was designed to allow double blind review (neither
author nor reviewer knows who the other is) of content posted to the web site.
In particular it was designed for review of grant proposals and written student
work. The idea was to provide this facility in as "plonish" a way as possible,
so that it could be used with almost any content type one could devise. In
particular, I wanted to create something that non-programmers could use for any
kind of submission they could build through the web using Dexterity. The main
impetus for this was that I foresee passing responsibility for my institution's
internal grant processing onto someone else in the near future.- May 16, 2013 -
Jonathan Gutow, University of Wisconsin Oshkosh, Oshkosh, WI, USA

*Administration Overview 
For each type of proposal or proposal cycle the
administrator creates a Proposal Drop Box with instructions in it for what to
submit and when. At the end of the submission period the administrator stops
accepting submissions by changing the workflow state. The administrator then
assigns reviewers to the proposals and changes the state of the Proposal Drop
Box and its contents to "under review". Content rules could be used to
automatically notify the assigned reviewers by e-mail that the proposals are
ready for review, but this is not set up by default. Once the reviewers are done
the proposals are passed on to the panel (another state change) for a final
decision, which is recorded by changing the state of the proposal, as well. When
everything is complete the drop box state is changed to cycle complete and the
decisions and reviews are made visible to the proposers.

*Submitting a Proposal Overview 
The proposer navigates to the web site. In general they should be directed to
the public landing page. Once they log in links will appear in the 
main navigation bar at the top of the page for any proposal 
drop boxes that are currently accepting submissions or under review.
Thus the landing page should describe what kind of an account is necessary to
access the site. Proposals for which the submission-review cycle is complete do
not show up in the main bar (the administrator is encouraged to make them
available through an "Archive" collection at the root level of the site). By
clicking on the link in the top navigation bar the proposer navigates to the
proposal drop box. Using the "Add New ..." menu they add a new proposal and
provide some basic information. Once the proposal is created they add proposer
ID and contact information to the proposal as sub items. In the examples
provided there are two types of proposers (proposers and mentors), allowing for
student proposers and faculty mentors to provide different information. The
proposer and mentor items follow their own workflows and are only visible to the
site manager and the proposer or mentor. This way the proposal can be anonymous
as long as the proposer avoids putting identifying information in the proposal.
A one or two tiered submission process is available. If the proposer is a member
of a group that is assigned the role of "submitter" they can directly submit the
proposal by selecting the "submit" option in the state menu. If the proposer is
not a member of the "submitter" group (students proposers are not allowed to
submit directly in our system), they cannot submit directly. They must "share"
their proposal with their mentor using the sharing tab and they also select the
"Send proposal to Advisor for approval and submission..." in the state menu. The
mentor can then submit it if they approve. The manager then assigns reviewers
using the sharing tab and transitions the proposal to the "Under Review" state.
Once decisions are made the whole drop box is converted to the "Cycle complete"
state and the decisions and reviews become visible to the proposer.

*How It Works 
This product defines a number of specialized workflows: 
A. Proposal Folder Workflow with the following state progression: 
  1. private (viewable by manager and owner) 
  2. Accepting Submissions (all logged in users can see and create
  proposals within the dropbox) 
  3. No longer Accepting submissions (visible to logged
  in users, but no proposals can be added) 
  4. Under Review (only reviewers can see proposals) 
  5. Under Panel Review (only panelists can see proposals) 
  6. Cycle Complete (visible to logged in users) 
B. Proposal Workflow with the following state progression: 
  1. Private (visible to and editable by owner, editor(s), manager)
  2. Advisor Review (visible to and editable by owner, editor(s), manager) 
  3. Submitted (visible to owner, editor(s) and editable by manager) 
  4. Under Review (visible to reviewer(s) and editable by manager) 
  5. Panel Review (visible to panelist(s) and editable by manager) 
  6. approved_invisible (visible to panelist(s) and editable by manager) 
  7. Approved (visible to owner, editor(s), reviewer(s) and editable by
  manager) 
  8. alternate_invisible (visible to panelist(s) and editable by manager)
  9. Alternate (visible to owner, editor(s), reviewer(s) and editable by manager)
  10. denied_invisible (visible to panelist(s) and editable by manager) 
  11. Denied (visible to owner, editor(s), reviewer(s) and editable by manager) 
C. ID info Workflow with only a private state (visible and editable by owner, 
  editor(s) and manager). 
D. Anonymous Peer Review Workflow with the following state progression:
  1. Private (visible to and editable by owner (aka reviewer) and manager) 
  2. Submitted (visible to owner (aka reviewer) and and editable by manager) 
  3. Under Panel Review (visible to panelist(s) and editable by manager) 
  4. Cycle Complete (visible to owner, reviewer(s), and panelist(s), editable 
  by manager) 
E. Instructor Only Workflow is an always private workflow only visible to managers. 

This product defines some Dexterity based content types as well: 
A. Web Page: It is intended as a replacement for the traditional Plone type 
  "Page". It has the advantage when building a product that it can be easily
  exported into a product using Portal_Setup in the ZMI (see Plone developer 
  documentation at Plone.org).  The instruction pages included in this product
  use clones of this type.
B. Proposal Drop Box: this is a container that follows the Proposal Folder
  Workflow. A new Proposal Drop Box with an appropriate title and a prominent
  warning about closing date should be created for each proposal cycle. This can
  be used as an assignment drop box for student work as well. 
C. mock proposal: this is a content type which is a simple example of 
  how to build a proposal. The key features are that it has an upload 
  button for uploading the submitted document and is a container into 
  which the proposer can add other documents, which may or may not be 
  viewable by the reviewers. This type follows the Proposal Workflow.
  Cloning this is a good place to start when building a proposal type for your
  site. 
D. Proposer: this is an example of the content type I use to contain
  information about the proposer that would compromise the anonymity of the
  proposer. It follows the ID info Workflow, making it invisible to anyone but the
  proposer and authenticated users with the role of Administrator. 
E. Mentor: this is an example of the content type I use to contain information 
  about the faculty mentor that would compromise the anonymity of 
  the proposing team. It follows the ID info Workflow, making it invisible to 
  anyone but the proposer and authenticated users with the role of Administrator.
