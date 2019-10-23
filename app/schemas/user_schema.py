from app import ma

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("public_id", "email", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("api.userbyidcontroller", public_id="<public_id>"), "collection": ma.URLFor("api.usercontroller")}
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)