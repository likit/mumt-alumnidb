"""added member info model

Revision ID: b2efdb1d8caf
Revises: 9ddddf4be827
Create Date: 2025-01-05 11:01:53.420272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2efdb1d8caf'
down_revision = '9ddddf4be827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('graduate_year', sa.String(), nullable=True),
    sa.Column('program', sa.String(), nullable=True),
    sa.Column('line_id', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('work_office', sa.Text(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_info')
    # ### end Alembic commands ###
