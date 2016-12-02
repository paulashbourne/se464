import flask

# A wrapper around a flask blueprint
# get, post, patch, and delete all wrap
# the route function, and apply the methods option
# corresponding to the function
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
