from django.contrib.auth.base_user import BaseUserManager


class ProductManager(BaseUserManager):
    use_in_migrations = True

    def _create_product(self, name, company_name, pro_date,image):

        if not name:
            raise ValueError('The given name must be set')
        name =  self.model(name=name)
        company_name = self.model(company_name=company_name, **extra_fields)
        .
        .
        .
        .
        product.save(using=self._db)
        return user

