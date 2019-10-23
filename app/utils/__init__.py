from app import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("api.userbyidcontroller", id="<id>"), "collection": ma.URLFor("api.usercontroller")}
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)