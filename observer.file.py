class Observer:

    def __init__(self, observable):
        observable.ready(self)

    def notify(
        self,
        observable,
        *args,
        **kwargs
        ):
        print ('Hello', args, kwargs, 'From', observable)

class Observable:

    def __init__(self):
        self._observers = []

    def ready(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unready(self, observer):
        self._observers.remove(observer)


subject = Observable()

machine1 = Observer(subject)
machine2 = Observer(subject)

subject.notify_observers('Jack I am ready to work',
                         kw='From machine1')
subject.unready(machine2)

subject.notify_observers('Jack I am currently doing a task',
                         kw='From the machine2')