import alexandria as ax
#import readline
import code


def create_new_record(data, Model):
    record = Model(**data)
    ax.db_session.add(record)
    ax.db_session.commit()
    print(record)


def new_book():
    create_new_record(
        input_data(ax.Book),
        ax.Book)


def new_student():
    create_new_record(
        input_data(ax.Student),
        ax.Student)


def new_author():
    create_new_record(
        input_data(ax.Author),
        ax.Author)


def input_data(Model):
    model_data = {}
    print("collecting data for", Model.modelname)

    for field in Model.export:
        if field not in ['id', 'identity',
                         "creation_time", "author",
                         'borrowed']:
            model_data[field] = input("give me %s: " % field)

    if Model == ax.Book:
        a_data = {
            'name': input("give me name of author: "),
            'surename': input("give me surename of author: ")
        }
        author = ax.Author.query.filter(
            ax.Author.name == a_data['name']
            and ax.Author.surename == a_data['surename']
        ).first()
        if author:
            model_data['author'] = author
        else:
            print("adding new author")
            author = ax.Author(**a_data)
            model_data['author'] = author
    return model_data


if __name__ == "__main__":
    ax.init_db(overwrite=False)
    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    print("enter commands here!")
    print("choices: new_author(), new_student(), new_book()")
    shell.interact()


