"""replaced file_url with filename

Revision ID: 6f70dc42f6f0
Revises: 0dd192866f1b
Create Date: 2024-12-20 08:57:44.362025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f70dc42f6f0'
down_revision = '0dd192866f1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_ticket_payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.String(), nullable=True))
        batch_op.drop_column('file_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_ticket_payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_url', sa.VARCHAR(), autoincrement=False, nullable=True))
        batch_op.drop_column('filename')

    # ### end Alembic commands ###