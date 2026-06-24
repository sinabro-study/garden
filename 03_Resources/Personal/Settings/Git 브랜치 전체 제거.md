```shell
exclude_branches=("main")
branches=$(git branch -v | awk '{ if ($1 ~ /^\*/) print $2; else print $1 }')

filtered_branches=()

for branch in ${branches[@]}; do
    skip_branch=false
    for excluded_branch in ${exclude_branches[@]}; do
        if [[ "$branch" == "$excluded_branch" ]]; then
            skip_branch=true
            break
        fi
    done

    if [ "$skip_branch" = false ]; then
        filtered_branches+=("$branch")
    fi
done

for branch in $filtered_branches; do
  git branch -D $branch
done
```
