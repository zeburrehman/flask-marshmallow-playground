"""Appointment_Table_Added

Revision ID: 74f169b0890c
Revises: 2995eea7b27d
Create Date: 2019-10-24 10:34:03.758585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f169b0890c'
down_revision = '2995eea7b27d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('service_provider_id', sa.Integer(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['service_provider_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointment')
    # ### end Alembic commands ###
