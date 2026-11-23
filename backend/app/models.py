from datetime import datetime
from sqlalchemy import ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Repo(Base):
    __tablename__ = "repos"
    __table_args__ = (UniqueConstraint("owner", "name"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str]
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    last_synced_at: Mapped[datetime | None]

class PrRecord(Base):
    __tablename__ = "pr_records"
    __table_args__ = (UniqueConstraint("repo_id", "number"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    repo_id: Mapped[int] = mapped_column(ForeignKey("repos.id", ondelete="CASCADE"))
    number: Mapped[int]
    created_at: Mapped[datetime]
    merged_at: Mapped[datetime | None]

class IssueRecord(Base):
    __tablename__ = "issue_records"
    __table_args__ = (UniqueConstraint("repo_id", "number"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    repo_id: Mapped[int] = mapped_column(ForeignKey("repos.id", ondelete="CASCADE"))
    number: Mapped[int]
    created_at: Mapped[datetime]
    first_response_at: Mapped[datetime | None]

class Snapshot(Base):
    __tablename__ = "snapshots"
    id: Mapped[int] = mapped_column(primary_key=True)
    repo_id: Mapped[int] = mapped_column(ForeignKey("repos.id", ondelete="CASCADE"))
    taken_at: Mapped[datetime] = mapped_column(server_default=func.now())
    median_pr_merge_hours: Mapped[float | None]
    median_issue_response_hours: Mapped[float | None]
    bus_factor: Mapped[int | None]
    health_score: Mapped[int | None]