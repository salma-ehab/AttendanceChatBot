from main import db,Attendee


def addAttendee(attendeeName,attendeeID):
    name = ' '.join(attendeeName)
    id=int(attendeeID[0])
    newAttendee = Attendee(name=name,id=id)

    try:
        db.session.add(newAttendee)
        db.session.commit()
        return 1

    except:
        print("There was an issue")
        return 0






