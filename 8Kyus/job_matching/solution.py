def job_matching(candidate, job):
    if not candidate["min_salary"] or not job["max_salary"]:
        return None
    if candidate["min_salary"] - (candidate["min_salary"] * 0.10) <= job["max_salary"]:
        return True
    return False


if __name__ == "__main__":
    candidate2 = {"min_salary": 190000}
    job3 = {"max_salary": 171000}
    print(job_matching(candidate2, job3))