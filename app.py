import flask

class App(flask.Flask):

    def get(self, *args, **kwargs):
        kwargs['methods'] = ['GET']
        return self.route(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs['methods'] = ['POST']
        return self.route(*args, **kwargs)

    def patch(self, *args, **kwargs):
        kwargs['methods'] = ['PATCH']
        return self.route(*args, **kwargs)

    def delete(self, *args, **kwargs):
        kwargs['methods'] = ['DELETE']
        return self.route(*args, **kwargs)

class Blueprint(flask.Blueprint):

    def get(self, *args, **kwargs):
        kwargs['methods'] = ['GET']
        return self.route(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs['methods'] = ['POST']
        return self.route(*args, **kwargs)

    def patch(self, *args, **kwargs):
        kwargs['methods'] = ['PATCH']
        return self.route(*args, **kwargs)

    def delete(self, *args, **kwargs):
        kwargs['methods'] = ['DELETE']
        return self.route(*args, **kwargs)
