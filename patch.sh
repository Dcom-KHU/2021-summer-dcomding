echo starting patch...
for user in $(git branch -r | cut -d '/' -f 2)
do
    git checkout $user
    git pull
    git merge master --no-edit
    git push origin $user
done
echo patch finished!