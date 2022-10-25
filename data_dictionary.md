# Hackathon Data

1. **Navigation Events**
1. **Additional** - this data was pulled using the Canvas API. Included here is the *Official Information* - which is the detailed API and data information from Canvas. We have also included *Field Descriptions* for each additional data source. The field descriptions indicates which fields from the API are kept, and provides more information about the data. Where necessary, notes are added to help understand this data more thoroughly. 
   
## Navigation Events
> navigation_events.csv

## Assignments 
- File: additional/assignments.csv
- Official Information: https://canvas.instructure.com/doc/api/assignments.html

### Field Descriptions

Field | Type | Description | Note
---------|----------|---------|---------
 id | assignment_id | The assignment_id is a unique identifier of an assignment | 
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

## Enrollments
> additional/enrollments.csv

## Files
> additional/files.csv

## Module Items
> additional/module_items.csv

## Pages
> additional/pages.csv