# Pandas 5 HW Solutions

# Problem 1 : Department Highest Salary

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee[['departmentId','salary']].sort_values(by = ['salary'], ascending=False)
    df.drop_duplicates(subset=['departmentId'],inplace=True)
    df2 = employee.merge(df)
    df3 = df2.merge(department, left_on = 'departmentId',right_on='id')
    return df3[['name_y','name_x','salary']].rename(columns = {'name_y' : 'Department', 'name_x' : 'Employee'})




# Problem 2 : Rank Scores


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores[['score','rank']].sort_values(['score'],ascending=False)