# AndroidX multiplatform adoption

AndroidX libraries are expanding to KMP, but support differs by library, version, target, and feature.

For each candidate:

1. Check the current official KMP support page.
2. Confirm exact artifacts and targets.
3. Check whether the API is stable, beta, alpha, or experimental.
4. Check setup differences per platform.
5. Compare repository ownership boundaries.
6. Test migration and stored-data compatibility where applicable.

Current official entry points:

- AndroidX KMP overview: https://developer.android.com/kotlin/multiplatform
- Room KMP: https://developer.android.com/kotlin/multiplatform/room
- DataStore KMP: https://developer.android.com/kotlin/multiplatform/datastore
- ViewModel KMP: https://developer.android.com/kotlin/multiplatform/viewmodel

Do not assume:

- every AndroidX library is portable
- every target has identical persistence or lifecycle behavior
- adopting a KMP library means UI or OS integration should move to common code
- a current supported target existed in older documentation
