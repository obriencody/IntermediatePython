import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, memo, tags=""):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self._memo = memo
        self._tags = tags
        self._creation_date = datetime.date.today()
        global last_id
        last_id += 1

        self._id = last_id

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags."""
        return filter in self._memo or filter in self._tags


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list."""
        self._notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list."""
        self._notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self._notes:
            if note._id == note_id:
                return note
        return None


    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        # for note in self._notes:
        #     if note._id == note_id:
        #         note._memo = memo
        #         break
        self._find_note(note_id)._memo = memo

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        # for note in self._notes:
        #     if note._id == note_id:
        #         note._tags = tags
        #         break

        self._find_note(note_id)._tags = tags

    def search(self, filter):
        """Find all notes that match the given filter
        string."""
        return [note for note in self._notes if note.match(filter)]


def main():
    # n1 = Note('hello first')
    # n2 = Note('hello again', 'hi')
    # print(n1._id, n1._memo)
    # print(n2._id, n2._memo)
    # print(n1.match('hello'))
    # print(n2.match('hi'))
    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    print(n._notes)
    print(n._notes[0]._id)
    print(n._notes[0]._memo)
    print(len(n.search('hello')))
    n.modify_memo(1, 'hi world')
    print(n._notes[0]._memo)
    n.modify_tags(1, 'hi guys')
    print(n._notes[0]._tags)

if __name__ == "__main__":
    main()