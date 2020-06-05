### Useful commands
```
curl <link> | jq '.'
cat <filename>.json | jq '.'
cat <filename>.json | jq '.[] | { message: .commit.message, name: .commit.committer.name}'
cat <filename>.json | jq '[.[] | { message: .commit.message, name: .commit.committer.name}]'
cat <filename>.json | jq '[.[] | { message: .commit.message, name: \
               .commit.committer.name, parent: [.parents[].html_url]}]'
cat <filename>.json | jq '.id'
cat <filename>.json | jq '.name.first'
cat <filename>.json | jq '.id.fec[-1]'
cat <filename>.json | jq '.terms[0].start'
```

#### Reference

[jq download](https://github.com/stedolan/jq/tree/master/src)
