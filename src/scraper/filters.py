thondef apply_filters(results, filters):
    keyword = filters.get("keyword")
    if keyword:
        results = [r for r in results if keyword.lower() in r["job_title"].lower()]
    return results