import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Union

from pydantic import BaseModel

from .model_interface import ModelMeta


class TaskResult(BaseModel):
    task_name: str
    task_description: str
    task_version: str
    time_of_run: datetime
    scores: Dict[str, Dict[str, float]]  # {language: {"metric": value}}.
    main_score: str

    def get_main_score(self, lang: Optional[Iterable[str]] = None) -> float:
        main_scores = []
        if lang is None:
            lang = self.scores.keys()

        for l in lang:
            main_scores.append(self.scores[l][self.main_score])

        return sum(main_scores) / len(main_scores)

    @property
    def languages(self) -> List[str]:
        return list(self.scores.keys())

    @classmethod
    def from_disk(cls, path: Path) -> "TaskResult":
        """
        Load task results from a path.
        """
        with open(path, "r") as f:
            task_results = json.load(f)
        return cls(**task_results)

    def to_disk(self, path: Path) -> None:
        """
        Write task results to a path.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        json_str: str = self.model_dump_json()

        with open(path, "w") as f:
            f.write(json_str)


class TaskError(BaseModel):
    task_name: str
    error: str
    time_of_run: datetime

    def to_disk(self, path: Path) -> None:
        """
        Write task results to a path.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        json_str: str = self.model_dump_json()

        with open(path, "w") as f:
            f.write(json_str)

    @classmethod
    def from_disk(cls, path: Path) -> "TaskError":
        """
        Load task results from a path.
        """
        with open(path, "r") as f:
            task_results = json.load(f)
        return cls(**task_results)

    @staticmethod
    def get_main_score(lang: Optional[Iterable[str]] = None) -> None:
        return None


class BenchmarkResults(BaseModel):
    meta: ModelMeta
    task_results: List[Union[TaskResult, TaskError]]

    def __iter__(self) -> Iterator[Union[TaskResult, TaskError]]:
        return iter(self.task_results)

    def __getitem__(self, index: int) -> Union[TaskResult, TaskError]:
        return self.task_results[index]

    def __len__(self) -> int:
        return len(self.task_results)
