from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-collective.js.webshims:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
