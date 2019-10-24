from app import ma

class AppointmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("patient.last_name", "service_provider.last_name")


appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)