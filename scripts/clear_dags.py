import subprocess
from dataclasses import dataclass
from datetime import datetime
from loguru import logger
from croniter import croniter_range

@dataclass
class DagRun:
    dag_id: str
    schedule_interval: str = "0 * * * *"

SILVER_DEPENDENT_DAGS=(
    # DagRun("X3M_DAU", "0 0 * * *"),
    # DagRun("X3MInstancesStatsDailySummarization", "0 0 * * *"),
    # DagRun("X3MInstancesStatsHourlySummarization", "0 0 * * *"),
    # DagRun("X3MWaterfallsStatsDailySummarization", "0 0 * * *"),
    # DagRun("X3MWaterfallsStatsHourlySummarization", "0 0 * * *"),
    # DagRun("X3MABTestSummarization"),
    # DagRun("X3MAppsSummarization"),
    # DagRun("X3MInstanceSummarization"),
    # DagRun("X3MWaterfallsSummarization"),
    # DagRun("X3MInstanceErrorsSummarization_Lake_V2"),
    DagRun("X3MWaterfallsStatsHourlySummarizationReprocess", "30 * * * *"),
)

ENV="prd" # "stg"
BASE_DAG_RUN_CLEAR_CMD=f"python airflow-cli.py --env {ENV} dag-runs clear {{dag_id}} {{dag_run_id}}"

START_DATE = datetime(2023, 3, 13)
END_DATE = datetime(2023, 3, 21)

for dag_run in SILVER_DEPENDENT_DAGS:
    dag_id = dag_run.dag_id
    schedule_interval = dag_run.schedule_interval

    date_range = croniter_range(
        start=START_DATE,
        stop=END_DATE,
        expr_format=schedule_interval,
        ret_type=datetime
    )

    for logical_date in date_range:
        dag_run_id = f"scheduled__{logical_date.strftime('%Y-%m-%dT%H:%M:%S+00:00')}"
        cmd = BASE_DAG_RUN_CLEAR_CMD.format(dag_id=dag_id, dag_run_id=dag_run_id)
        logger.info("Running command: {}", cmd)
        subprocess.run(cmd, shell=True, check=True)
