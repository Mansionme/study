"""empty message

Revision ID: ec4b86fef7b1
Revises: 
Create Date: 2020-05-01 20:05:20.021707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4b86fef7b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('department_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('department_name')
    )
    op.create_table('teach_plan',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('remarks', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=10), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('week_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subject')
    )
    op.create_table('teach_weeks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('term', sa.String(length=30), nullable=False),
    sa.Column('week_start', sa.Date(), nullable=False),
    sa.Column('week_end', sa.Date(), nullable=False),
    sa.Column('weekno_term', sa.String(length=30), nullable=False),
    sa.Column('week_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('term'),
    sa.UniqueConstraint('week_end'),
    sa.UniqueConstraint('week_no'),
    sa.UniqueConstraint('week_start'),
    sa.UniqueConstraint('weekno_term')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teach_weeks')
    op.drop_table('teach_plan')
    op.drop_table('department')
    # ### end Alembic commands ###
