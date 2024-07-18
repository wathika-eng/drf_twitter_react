/* python manage.py sqlflush delete whole DB*/ BEGIN;

DELETE FROM "django_admin_log";

DELETE FROM "auth_user_user_permissions";

DELETE FROM "auth_group_permissions";

DELETE FROM "auth_user_groups";

DELETE FROM "auth_user";

DELETE FROM "django_content_type";

DELETE FROM "django_session";

DELETE FROM "auth_group";

DELETE FROM "auth_permission";

DELETE FROM "drfapi_advocate";

UPDATE "sqlite_sequence"
SET
    "seq" = 0
WHERE
    "name" IN (
        'django_admin_log',
        'auth_user_user_permissions',
        'auth_group_permissions',
        'auth_user_groups',
        'auth_user',
        'django_content_type',
        'django_session',
        'auth_group',
        'auth_permission',
        'drfapi_advocate'
    );

COMMIT;