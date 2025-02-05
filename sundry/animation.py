text = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!74 &7400000
AnimationClip:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_Name: Data-$index-$mark
  serializedVersion: 7
  m_Legacy: 0
  m_Compressed: 0
  m_UseHighQualityCurve: 1
  m_RotationCurves: []
  m_CompressedRotationCurves: []
  m_EulerCurves: []
  m_PositionCurves: []
  m_ScaleCurves: []
  m_FloatCurves:
  - serializedVersion: 2
    curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: $value
        inSlope: 0
        outSlope: 60
        tangentMode: 69
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    attribute: material._Byte$index
    path: 
    classID: 23
    script: {fileID: 0}
    flags: 0
  m_PPtrCurves: []
  m_SampleRate: 60
  m_WrapMode: 0
  m_Bounds:
    m_Center: {x: 0, y: 0, z: 0}
    m_Extent: {x: 0, y: 0, z: 0}
  m_ClipBindingConstant:
    genericBindings:
    - serializedVersion: 2
      path: 0
      attribute: 2243268732
      script: {fileID: 0}
      typeID: 23
      customType: 22
      isPPtrCurve: 0
      isIntCurve: 0
      isSerializeReferenceCurve: 0
    pptrCurveMapping: []
  m_AnimationClipSettings:
    serializedVersion: 2
    m_AdditiveReferencePoseClip: {fileID: 0}
    m_AdditiveReferencePoseTime: 0
    m_StartTime: 0
    m_StopTime: 0
    m_OrientationOffsetY: 0
    m_Level: 0
    m_CycleOffset: 0
    m_HasAdditiveReferencePose: 0
    m_LoopTime: 0
    m_LoopBlend: 0
    m_LoopBlendOrientation: 0
    m_LoopBlendPositionY: 0
    m_LoopBlendPositionXZ: 0
    m_KeepOriginalOrientation: 0
    m_KeepOriginalPositionY: 1
    m_KeepOriginalPositionXZ: 0
    m_HeightFromFeet: 0
    m_Mirror: 0
  m_EditorCurves:
  - serializedVersion: 2
    curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: $value
        inSlope: 0
        outSlope: 60
        tangentMode: 69
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    attribute: material._Byte$index
    path: 
    classID: 23
    script: {fileID: 0}
    flags: 0
  m_EulerEditorCurves: []
  m_HasGenericRootTransform: 0
  m_HasMotionFloatCurves: 0
  m_Events: []

"""

for i in range(256):
    with open(f"anim/Data-{i}-A.anim", "w") as f:
        f.write(text.replace("$value", "0").replace("$mark", 'A').replace("$index", str(i)))
    with open(f"anim/Data-{i}-B.anim", "w") as f:
        f.write(text.replace("$value", "255").replace("$mark", 'B').replace("$index", str(i)))