from celery import shared_task


@shared_task
def merge_resources_task(
    user_id,
    base_resource_id,
    merge_resource_id,
    merge_tracker_resource_id=None,
    overwrite_multiple_tiles=False,
):
    raise NotImplementedError("Not relevant for public-facing site")
