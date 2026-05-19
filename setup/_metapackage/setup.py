import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-simetri-sinergi-id-ssi-mixin",
    description="Meta package for simetri-sinergi-id-ssi-mixin Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-ssi_company_currency_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_decorator>=15.0dev,<15.1dev',
        'odoo-addon-ssi_master_data_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_multiple_approval_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_policy_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_print_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_product_line_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_product_line_price_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_sequence_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_cancel_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_confirm_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_done_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_open_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_ready_mixin>=15.0dev,<15.1dev',
        'odoo-addon-ssi_transaction_terminate_mixin>=15.0dev,<15.1dev',
        'odoo-addon-test_ssi_master_data_mixin>=15.0dev,<15.1dev',
        'odoo-addon-test_ssi_transaction_mixin>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
