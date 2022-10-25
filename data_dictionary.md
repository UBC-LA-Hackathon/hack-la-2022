# Hackathon Data

1. **Navigation Events**: Student-level navigation events in a given Canvas course. This dataset has been simplified and anonymized for the purpose of this hackathon as described in the Field Descriptions below. 
Original Navigation Events (not used in this hackathon) are in the following format: https://canvas.instructure.com/doc/api/file.data_service_caliper_navigation_events.html 

2. **Additional**: this data was pulled using the Canvas API. Included here is the *Official Information* - which is the detailed API and data information from Canvas. We have also included *Field Descriptions* for each additional data source. The field descriptions indicates which fields from the API are kept, and provides more information about the data. Where necessary, notes are added to help understand this data more thoroughly. 
   
## Navigation Events
> navigation_events.csv

Navigation events are a type of Caliper event. There are different "types" of navigation events based on the kind of event (the type and subtype). In the original data, Caliper events are in JSON format and each event includes a list of "data". In the transformed csv, each item in the data list is an "event". The field will contain the prefix event__ for each. 
### Field Descriptions

Field | Type | Description | Note
---------|----------|---------|---------
type | string | The type of event | all event types in this data are NavigationEvent
action 
event_time | datetime | The datetime of the event action
session_id | id string | When a user performs a series of actions within a certain timeframe (between action or inaction), or between logins - this is categorized as a single session | TODO - how Canvas defines a session
membership_role | list | The  
membership_type 
event__id
event__type
event__actor_type
event__action
event__object_type
event__object_name
event__object_extensions_asset_type
event__object_extensions_http_method
event__eventTime
event__edApp_type
event__session_type
object_id_type
event__object_id_type
event__attachment_type
object_id
event__object_extensions_asset_name
actor_id
## Module Items
> File: additional/module_items.csv
> Official Information: (module), (module item)

In Canvas, content can be organized into Modules which contain module items. Module items can be pages, files, assignments, quizzes, discussion forums etc. Module items can be published/unpublished, if they are assignments they can have due dates, and if they are pages/files they can have to-do dates. Modules can be organized in any way, could have requirements and/or pre-requisites and may be published/unpublished.  

![module and items](imgs/modules_instructor_view.png)


### Field Descriptions

Field | Type | Description | Note
---------|----------|---------|---------

## Assignments 
- File: additional/assignments.csv
- Official Information: https://canvas.instructure.com/doc/api/assignments.html

Assignments are any sort of assessible content in Canvas - this may include an Assignment, Quiz, or Graded Discussion. Assignments can be found in the Assignments navigation (when set to visible by the instructor), and/or included as a module item - this depends on the decisions of individual course instructors. Instructors can choose to organize Assignments in groups for organizational (as done in the example Assignments area below) and/or grading purposes (i.e. creates weighting for group of assignments). 

> For the purposes of the hackathon, assume that all Assignments are 

![assignments](imgs/assignments_instructor_view.png)

### Field Descriptions

Field | Type | Description | Note
---------|----------|---------|---------
 id | assignment_id | The assignment_id is a unique identifier of an assignment | The assignment_id has been anonymized for the purpose of the hackathon (it is typically an integer)
 due_at | datetime | The due date of the assignment
 unlock_at | datetime | The datetime of when to unlock the assignment (make it accessible to students) | If empty, there is no lock / unlock dates for this assignment
 lock_at | datetime | The datetime of when to lock the assignment (make it inaccessible to students) | If empty, there is no lock / unlock dates for this assignment
 points_possible | number | The total points available for grading in this assignment 
 grading_type | string | How to assign grades to the assignment
 position | number | In a Canvas course instructors can organize assignments into groups - when doing so, the position indicates the assignment sort order within its group 
 name | string | The assignment name
 submission_types | list | The possible assignment submission types
 has_submitted_submissions | boolean | Whether any submissions have been submitted for the given assignment
 workflow_state | string | The state of the assignment within the course | Typically published or unpublished 
 published | boolean | The published state of a given assignment


## Discussion Topics
> File: additional/discussion_topics.csv
> Official Information: https://canvas.instructure.com/doc/api/discussion_topics.html

## Files
> additional/files.csv

## Pages
> additional/pages.csv

## Enrollments
> additional/enrollments.csv
