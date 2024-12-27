"""added key field to the payment slip model

Revision ID: af38be27fc2c
Revises: 6f70dc42f6f0
Create Date: 2024-12-20 20:55:40.162978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af38be27fc2c'
down_revision = '6f70dc42f6f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_ticket_payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('key', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_ticket_payments', schema=None) as batch_op:
        batch_op.drop_column('key')

    # ### end Alembic commands ###
