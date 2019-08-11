**Please replace these instructions with a description of your change. The
'New Fields Only' section should be removed if your pull request
doesn't add any new fields.**

Thanks for your contribution!

A checklist is included below which helps us keep the code contributions
consistent and helps speed up the review process. You can add additional
commits to your pull request if you haven't met all of these points on your
first version.

**All Changes**

- [ ] Add an entry to the docs/changelog.rst describing the change.

- [ ] Add an entry for your name in the docs/authors.rst file if it's not
      already there.

**New Fields Only**

- [ ] Prefix the country code to all fields.

- [ ] Field names should be easily understood by developers from the target
      localflavor country. This means that English translations are usually
      not the best name unless it's for something standard like postal code,
      tax / VAT ID etc.

- [ ] Prefer '<country code>PostalCodeField' for postal codes as it's
      international English; ZipCode is a term specific to the United
      States postal system.

- [ ] Add meaningful tests. 100% test coverage is not required but all
      validation edge cases should be covered.

- [ ] Add `.. versionadded:: <next-version>` comment markers to new
      localflavors.

- [ ] Add documentation for all fields.
